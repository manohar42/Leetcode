class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def graph_generator(n,res,val):

            res.append(val)

            val*=10
            # print(res)
            if val <= n:
                for i in range(0,10):
                    if val+i <= n:
                        #print(val)
                        graph_generator(n,res,val+i)
                    else:
                        break

        for i in range(1,min(n+1,10)):
            graph_generator(n,res,i)
        # print(res)
        return res