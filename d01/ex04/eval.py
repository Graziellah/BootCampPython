class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if isinstance(coefs, list)  and isinstance(words,  list):
            if len(coefs) == len(words):
                zipped = zip(coefs,words)
                total = 0.0
                for elem in  zipped:
                    total += elem[0] * len(elem[1])
                return total
        return -1

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if isinstance(coefs, list)  and isinstance(words,  list):
            if len(coefs) == len(words):
                nb = len(coefs)
                total = 0.0
                for i in range(0,nb):
                    for c,value in enumerate(words[i]):
                        #print('coco', str(coefs[i]),  type(coefs[i]))
                        total += coefs[i]
                return total
        return -1


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))