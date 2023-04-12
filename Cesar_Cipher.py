class CesarCipher:

    def rot13(self, text: str):
        abc = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
        return (lambda y: "".join([abc[(abc.find(x) + 13) % 35] for x in y]))(text)

    def rot47(self, text: str):
        new = ""
        for x in text:
            if 33 <= ord(x) <= 126:
                new += chr((ord(x) + 47) % 94)
                print((ord(x) + 47) % 94)
        return new
