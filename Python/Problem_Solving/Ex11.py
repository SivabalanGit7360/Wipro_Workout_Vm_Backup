
s1 = "{{[]}(){}}"

a1 = s1.count("{")
a2 = s1.count("}")
b1 = s1.count("(")
b2 = s1.count(")")
c1 = s1.count("[")
c2 = s1.count("]")

if a1==a2 and b1==b2 and c1==c2:
    print("balanced")
else:
    print("unbalanced")