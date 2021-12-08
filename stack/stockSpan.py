class StockSpanner:

    def __init__(self):
        self.stack = []            

    def next(self, price: int) -> int:
        arr = self.stack
        curr_price,curr_span = price,1
        while(arr and arr[-1][0]<=curr_price):
            prev_price,prev_span = arr.pop()
            
            curr_span+=prev_span
        arr.append((curr_price,curr_span))
        return curr_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)