from collections import Counter
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        hand.sort()
        dict1 = dict(Counter(hand))
        for i in range(len(hand)):
            if dict1[hand[i]] > 0:
                gd = groupSize - 1
                dict1[hand[i]] -= 1
                num = hand[i]
                while gd > 0:
                    if num + 1 not in dict1 or dict1[num + 1] == 0:
                        return False

                    dict1[num + 1] -= 1
                    num += 1
                    gd -= 1
        return True