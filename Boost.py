"""

[----------------]
[   SET OBJECT   ]
[----------------]

"""
class Set:
    """ Set() -> new empty Set object
    Set(iterable) -> new Set object"""
    def __bool__(self):
        if(len(self.__lst) > 0): return True
        else: return False
    def __repr__(self):
        return str(self.__lst)
    def __eq__(self, lst):
        if(type(lst) != __class__): return False
        if(self.__lst == lst.__lst): return True
        else: return False
    def __neq__(self, lst):
        if(type(lst) != __class__): return True
        if(self.__lst != lst.__lst): return True
        else: return False
    def __init__(self, lst=[]):
        self.__lst = []
        try:
            for i in lst:
                if(i not in self.__lst): self.__lst.append(i)
        except TypeError:
            self.__lst = []
    def __add__(self, lst):
        templist = __class__(self.__lst)
        templist.update(lst)
        return templist
    def __sub__(self, lst):
        templist = __class__(self.__lst)
        templist.delete(lst)
        return templist
    def __getitem__(self, key):
        return self.__lst[key]
    def __setitem__(self, key, value):
        if(value in self.__lst): self.remove(value)
        self.__lst[key] = value
    def __delitem__(self, key):
        del self.__lst[key]
    def __iter__(self):
        return iter(self.__lst)
    def __reversed__(self):
        templist = list(self.__lst)
        templist.reverse()
        return iter(templist)
    def __contains__(self, item):
        if item in self.__lst: return True
        else: return False
    def __missing__(self, key):
        raise IndexError("Set index out of range")
    def __len__(self):
        return len(self.__lst)
    def add(self, obj):
        """ Set.add(obj) -> None -- add an element to a Set """
        if(obj not in self.__lst): self.__lst.append(obj)
    def remove(self, obj):
        """ Set.remove(obj) -> None -- remove an element from a Set
        Raises ValueError if the value is not present in the Set"""
        self.__lst.remove(obj)
    def discard(self, obj):
        """ Set.discard(obj) -> None -- remove an element from a Set, if it is a member """
        if(obj in self.__lst): self.__lst.remove(obj)
    def union(self, *lsts):
        """ Set.union(Sets) -> Set -- return union of Sets as a new Set """
        a = __class__(self.__lst)
        a.update(lsts)
        return a
    def update(self, *lsts):
        """ Set.update(Sets) -> None -- update a Set with contents of other Sets """
        for lst in lsts:
            if(type(lst) != __class__): raise TypeError("unsupported type "+str(type(lst)))
            for i in lst.__lst:
                if(i not in self.__lst): self.__lst.append(i)
    def delete(self, *lsts):
        """ Set.delete(Sets) -> None -- remove all elements of another Set from this Set"""
        for lst in lsts:
            if(type(lst) != __class__): raise TypeError("unsupported type "+str(type(lst)))
            for i in lst.__lst:
                if(i in self.__lst): self.__lst.remove(i)
    def intersection(self, *lsts):
        """ Set.intersection(Sets) -> Set -- return the intersection of two or more Sets as a new Set """
        a = __class__(self.__lst)
        a.intersection_update(lsts)
        return a
    def intersection_update(self, *lsts):
        """ Set.intersection_update(Sets) -> None -- update a Set with the intersection of itself and other lists """
        a = []
        for lst in lsts:
            if(type(lst) != __class__): raise TypeError("unsupported type "+str(type(lst)))
            for i in lst.__lst:
                if(i in self.__lst): a.append(i)
        self.__lst = a
    def intersecting(self, *lsts):
        """ Set.intersecting(Sets) -> bool -- return True if any elements of other Set are intersecting this Set """
        if(self.intersection(lsts) == []): return False
        else: return True
    def contains(self, *lsts):
        """ Set.contains(Sets) -> bool -- return True if this Set contains all elemets from other Sets """
        for lst in lsts:
            for i in lst.__lst:
                if(i not in self.__lst): return False
        return True
    def sort(self):
        """ Set.sort() -> None -- sort the Set"""
        self.__lst.sort()
    def reverse(self):
        """ Set.reverse() -> None -- reverse Sets elements order """
        self.__lst.reverse()
    def pop(self, indx):
        """ Set.pop(index) -> item -- remove and return Set element at index
        Raises IndexError if the Set is empty or index is out of range """
        return self.__lst.pop(indx)
    def index(self, obj):
        """ Set.index(value) -> int -- return first index of value
        Raises ValueError if the value is not present"""
        return self.__lst.index(obj)
    def clear(self):
        """ Set.clear() -> None -- removes all elements from Set """
        self.__lst.clear()
