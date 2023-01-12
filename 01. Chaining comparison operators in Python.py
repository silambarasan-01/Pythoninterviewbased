class demo:
    def matching(self):
        a = input(str("Enter the A value:"))
        b = input(str("Enter the B value:"))
        c = input(str("Enter the C value:"))

        if a == b == c:
            print(f'all are equal: {a}')
        elif a == b != c:
            print(f'a and b equal: {b}')
        elif a == c != b:
            print(f'a nad c is equal: {c}')
        else:
            #a != b == c:
            print(f'b nad c is equal: {c}')

obj=demo()
print(obj.matching())
