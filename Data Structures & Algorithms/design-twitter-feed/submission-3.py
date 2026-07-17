from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # { userId: set(userId, ...) }
        self.tweets = defaultdict(list) # { userId: [[tweetIndex, tweetId], ...] }
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCount += 1
        self.tweets[userId].append([self.tweetCount, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.tweets:
                index = len(self.tweets[user]) - 1
                tweetIndex, tweetId = self.tweets[user][index]
                maxHeap.append([tweetIndex, tweetId, user, index - 1])
        heapq.heapify_max(maxHeap)

        while maxHeap and len(res) < 10:
            tweetIndex, tweetId, user, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)

            if index >= 0 and user in self.tweets: 
                tweetIndex, tweetId = self.tweets[user][index]
                heapq.heappush_max(maxHeap, [tweetIndex, tweetId, user, index - 1])

        return res            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
