class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following[userId]:
            self.following[userId].add(userId)
        
        # timestamp, followingId, where in their posts are we 
        feed = []
        following = self.following[userId]
        for f in following:
            if not self.posts[f]:
                continue
            timestamp, tweetId = self.posts[f][-1]
            pos = len(self.posts[f]) - 1
            heapq.heappush(feed, (-timestamp, tweetId, f, pos))

        res = []
        while feed:
            if len(res) >= 10:
                break
            timestamp, tweetId, follow_id, pos = heapq.heappop(feed)
            res.append(tweetId)
            if pos - 1 >= 0:
                pos -= 1
                post = self.posts[follow_id][pos]
                heapq.heappush(feed, (-post[0], post[1], follow_id, pos))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

