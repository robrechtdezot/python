def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ''' sort and get first and last string + minimal length'''
        strs.sort()
        first = strs[0]
        last = strs[-1]
        min_len = min(len(first), len(last))

        '''itterate until first and last are not equal'''
        i = 0
        while i < min_len and first[i] == last[i]:
            i+=1      
            if i == 0: 
                return ''
        return first[:i]
        
