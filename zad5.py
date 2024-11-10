class RealString:
    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        if isinstance(other, str):
            other = RealString(other)
        return len(self.string) < len(other.string)

    def __gt__(self, other):
        if isinstance(other, str):
            other = RealString(other)
        return len(self.string) > len(other.string)


apple = RealString("Apple")
yabluko = RealString("Яблоко")

print(apple > yabluko)
print(yabluko > "Банан")
print("Груша" < yabluko)
