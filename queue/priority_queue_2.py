class PriorityQueue:
    def __init__(self):
        self._datas = [None];

    def enqueue(self, x):
        self._datas.append(x);
        self._evaporate();
    
    def _evaporate(self):
        child = len(self._datas) - 1;
        parent = child // 2;
        while (parent > 0 and self._datas[parent] < self._datas[child]):
            self._swap(parent, child);
            child = parent;
            parent //= 2;

    def dequeue(self):
        self._sink(1);
        ret = self._datas.pop();
        return (ret);

    def _sink(self, parent):
        l = parent * 2 if len(self._datas) - 1 >= parent * 2 else None; 
        r = parent * 2 + 1 if len(self._datas) - 1 >= parent * 2 + 1 else None;
        if not all([l, r]):
            return ;
        else:
            child = l;
            if r is not None:
                child = l if self._datas[l] >= self._datas[r] else r;
                self._swap(parent, child);
            self._sink(child); 
        
    def find_max(self):
        return self._datas[1] if len(self._datas) > 1 else None;

    def _swap(self, i1, i2):
        temp = self._datas[i1];
        self._datas[i1] = self._datas[i2];
        self._datas[i2] = temp;

    def __getitem__(self, i):
        return None;

    def __setitem__(self, idx, val):
        pass;

