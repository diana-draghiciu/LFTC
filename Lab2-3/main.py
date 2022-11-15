from scanner import Scanner
from symbolTable import ST

if __name__ == '__main__':
    st = ST()
    ct = ST()
    scanner = Scanner('p1.txt', st, ct)
    # st.addToST('abc', 4)
    # st.addToST('p', 5)
    # st.addToST('efg', 5)
    # st.addToST('abc', 3)
    # print(st.table)  # {0: [('abc', 4), ('p', 5)], 5: [('efg', 5)]}
    # print(st.getValue('abc'))  # 4