# テーブルの1行
def row(id, name, country):
    return "<tr><td>" + str(id) + "</td><td>" + name + "</td><td>" + country + "</td></tr>"

# HTMLのテーブル
def table(fruits):
    header = """
        <table>
        <tr>
        <th> ID </th>
        <th> フルーツ名 </th>
        <th> 原産国 </th>
        </tr>
        """ 
    rows = ""
    for fruit in fruits:
        rows += row(fruit.id, fruit.name, fruit.country)

    # 改行を取り除く前のテーブル
    rawTable = header + rows + "</table>"

    # 改行を取り除いた後のテーブル
    return rawTable.replace('\n', '')

