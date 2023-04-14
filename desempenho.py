from jinja2 import Template

template = Template("""<table>
          <tr>
            <th>Mês</th>
            <th>Faturamento</th>
            <th>Despesas</th>
            <th>Lucro</th>
          </tr>
          <tr>
            <td>Janeiro</td>
            <td>R${{mes1}}</td>
            <td>R${{des1}}</td>
            <td>R${{lucro1}}</td>
          </tr>
          <tr>
            <td>Fevereiro</td>
            <td>R${{mes2}}</td>
            <td>R${{des2}}</td>
            <td>R${{lucro2}}</td>
          </tr>
          <tr>
            <td>Março</td>
            <td>R${{mes3}}</td>
            <td>R${{des3}}</td>
            <td>R${{lucro3}}</td>
          </tr>
          <tr>
            <!--<td>Abril</td>
            <td>R${{mes4}}</td>
            <td>R${{des4}}</td>
            <td>R${{lucro4}}</td>
          </tr>
          <tr>
            <td>Maio</td>
            <td>R${{mes5}}</td>
            <td>R${{des5}}</td>
            <td>R${{lucro5}}</td>
          </tr>
          <tr>
            <td>Junho</td>
            <td>R$mes6-</td>
            <td>R$-des6-</td>
            <td>R$-lucro6-</td>
          </tr>
          <tr>
            <td>Julho</td>
            <td>R$-mes7-</td>
            <td>R$-des7-</td>
            <td>R$-lucro7-</td>
          </tr>
          <tr>
            <td>Agosto</td>
            <td>R$-mes8-</td>
            <td>R$-des8-</td>
            <td>R$-lucro8-</td>
          </tr>
          <tr>
            <td>Setembro</td>
            <td>R$-mes9-</td>
            <td>R$-des9-</td>
            <td>R$-lucro9-</td>
          </tr>
          <tr>
            <td>Outubro</td>
            <td>R$-mes10-</td>
            <td>R$-des10-</td>
            <td>R$-lucro10-</td>
          </tr>
          <tr>
            <td>Novembro</td>
            <td>R$-mes11-</td>
            <td>R$-des11-</td>
            <td>R$-lucro11-</td>
          </tr>
          <tr>
            <td>Dezembro</td>
            <td>R$-mes12-</td>
            <td>R$-des12-</td>
            <td>R$-lucro12-</td>
          </tr>-->
</table>
""")


# Variáveis de faturamento:
 
mes1 = 10000
mes2 = 12000
mes3 = 13800
mes4 = 7543
# mes5 = 
# mes6 = 
# mes7 = 
# mes8 = 
# mes9 = 
# mes10 = 
# mes11 = 
# mes12 = 

# Variáveis de despesas:
des1 = 5677
des2 = 6543
des3 = 1356
des4 = 1299
# des5 = 
# des6 = 
# des7 = 
# des8 = 
# des9 = 
# des10 = 
# des11 = 
# des12 = 

# Cálculo do lucro
lucro1 = mes1 - des1
lucro2 = mes2 - des2
lucro3 = mes3 - des3
lucro4 = mes4 - des4
# lucro5 = mes5 - des5
# lucro6 = mes6 - des6
# lucro7 = mes7 - des7
# lucro8 = mes8 - des8
# lucro9 = mes9 - des9
# lucro10 = mes10 - des10
# lucro11 = mes11 - des11
# lucro12 = mes12 - des12

html = template.render(mes1=mes1, des1=des1, lucro1=lucro1, 
                      mes2=mes2, des2=des2, lucro2=lucro2, 
                      mes3=mes3, des3=des3, lucro3=lucro3, 
                      mes4=mes4, des4=des4, lucro4=lucro4,
                      # mes5=mes5, des5=des5, lucro5=lucro5,
                      # mes6=mes6, des6=des6, lucro6=lucro6,
                      # mes7=mes7, des7=des7, lucro7=lucro7,
                      # mes8=mes8, des8=des8, lucro8=lucro8,
                      # mes9=mes9, des9=des9, lucro9=lucro9,
                      # mes10=mes10, des10=des10, lucro10=lucro10,
                      # mes11=mes11, des11=des11, lucro11=lucro11,
                      # mes12=mes12, des12=des12, lucro12=lucro12
) 

print(html)