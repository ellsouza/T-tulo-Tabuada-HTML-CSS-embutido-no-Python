import html as _html

codigo = """#for 

print("Utilizando for:")
numero_usuario = int(input("Digite um número: "))

print("Tabuada do número", numero_usuario)

for numero in range (1,11):
    print(numero_usuario, "x", numero, "=", numero_usuario * numero)


#while

print("Utilizando while: contador é definido como 1 e multiplicado por 2 respeitando a condição de ser maior ou igual a 2 ")
contador = 1
while contador <= 10:
    print(contador * 2)
    contador += 1
"""

codigo_html = _html.escape(codigo)

html = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Tabuada</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Arial, sans-serif; background: #f6f6f6; }}
    .caixa {{
      max-width: 520px;
      margin: 40px auto;
      padding: 16px;
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 8px;
    }}
    pre {{
      margin: 0;
      padding: 12px;
      background: #fafafa;
      border: 1px solid #e5e5e5;
      border-radius: 6px;
      overflow: auto;
      white-space: pre-wrap;
      font-family: Consolas, "Courier New", monospace;
      font-size: 14px;
      line-height: 1.4;
    }}
  </style>
</head>
<body>
  <div class="caixa">
    <pre>{codigo_html}</pre>
  </div>
</body>
</html>
"""


