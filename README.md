# 🔍 ModSecurity Bypass Scanner v1.1
Ferramenta para testes de bypass em ModSecurity (WAF) com payloads variados, suporte a detecção básica de WAF, geração de logs e integração opcional com sqlmap.

⚠ Uso exclusivo para fins educacionais, auditorias de segurança e ambientes controlados. Não utilize em sistemas sem autorização.

📜 Recursos Principais
✔ Banner estilizado e informações do sistema
✔ Detecção simples de WAF (ModSecurity ou similar)
✔ Teste automatizado de payloads com indicadores de possível bypass
✔ Suporte a SQL Injection Time-based (detecta atrasos na resposta)
✔ Geração de dois relatórios:

resultado_scan.txt → log completo

bypass_detectados.txt → payloads que possivelmente funcionaram
✔ Integração com sqlmap para exploração automática (opcional)
✔ Código colorido no terminal para melhor visualização

# 🛠 Requisitos
Python 3.x

Bibliotecas Python:

pip install requests colorama
sqlmap (opcional, para exploração):
sudo apt install sqlmap

# ▶ Como Usar
Clone o repositório:

git clone https://github.com/K1r4-Fr13nd5/ModSecurity-Bypass-Scanner.git
cd ModSecurity-Bypass-Scanner-FS

Dê permissão de execução (opcional):
chmod +x modsecurity_bypass_scanner.py

Execute a ferramenta:
python3 modsecurity_bypass_scanner.py

# 🔍 Fluxo da Ferramenta
O script exibirá um banner com informações do sistema e quantidade de payloads.

Será solicitado que você insira a URL alvo (ex: http://alvo.com/busca.php).

A ferramenta:

Testa se há WAF detectável.

Realiza os testes com payloads ofuscados para bypass.

Identifica possíveis bypasses e SQLi Time-based.

Ao final:

Resultados completos → resultado_scan.txt

Payloads que possivelmente passaram pelo WAF → bypass_detectados.txt

Perguntará se você deseja rodar sqlmap automaticamente com evasão.

# 📂 Arquivos Gerados
resultado_scan.txt → Registro detalhado (payload, status HTTP, tempo, tamanho da resposta).

bypass_detectados.txt → Lista de payloads que podem ter funcionado.

⚡ Exemplo de Execução

$ python3 modsecurity_bypass_scanner.py

[?] Digite a URL alvo (ex: http://alvo.com/busca.php): http://teste.com/search.php
[+] Checando presença de WAF (ModSecurity)...
[✔] Nenhum WAF aparente detectado.

[1] Testando payload: ' OR 1=1--
    [+] Possível bypass! Código: 200 | Tempo: 0.45s
...
[+] Resultados completos salvos em: resultado_scan.txt
[+] Payloads com bypass salvos em: bypass_detectados.txt

[?] Deseja usar sqlmap automaticamente nesta URL? (s/n):

# 🧩 Personalização
Adicione mais payloads no array payloads[] no código.

Ajuste headers HTTP ou parâmetros de envio.

Habilite sqlmap para exploração pós-varredura.

⚠ Aviso Legal
O uso desta ferramenta para atacar alvos sem autorização é ilegal. O autor não se responsabiliza por usos indevidos. Utilize apenas em ambientes onde você tenha permissão explícita para realizar testes.

📌 Autor: K1r4_Fr13nd5
☠ Sociedade Fr13nd5

