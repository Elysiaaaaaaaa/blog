users = dict()  # 存用户信息
essays = dict()     # 存文章信息


class user:
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.essay = []         # 此用户的发文        标题    列表
        self.collection = []    # 存储用户收藏的文章   标题    列表
        users[username] = self  # 将user对象存储在users字典中，以username为key

    @staticmethod   # 静态方法
    def log(username, password):    # 用于比对用户是否已经注册，实现登录功能
        if username in users.keys():    # 检查username是否存在于users字典的键中
            if users[username].password == password:    # 比对密码和用户输入的密码
                return True
        return False



class essay:
    def __init__(self, es):
        self.title = es['title']    # 标题
        self.introduce = es['introduce']    # 简介
        self.text = es['text']  # 文本
        self.writer = es['writer']  # 作者
        self.review = es['review']  # 评论
        self.star = 0   # 点赞
        essays[self.title] = self   # 将essay对象存储在essays字典中，以title为键
        users[es['writer']].essay.append(es['title'])
        #   将essay对象的titles属性添加到用户的essay列表中
        #   es0 = {
        #     'title': '测试文章',
        #     'introduce':'测试简介',
        #     'text': "测试文本",
        #     'writer': "测试用户",
        #     'review': []    记录评论，每条评论为[评论用户名,评论内容]形式
        # }


u = user("1","1")
u1 = user('测试用户', '1')


es0 = {
    'title': '测试文章',
    'introduce':'测试简介',
    'text': "测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本",
    'writer': "测试用户",
    'review': []
}
e0 = essay(es0)

es1 = {
    'title': '爬天梯',
    'introduce':'递归，动态规划',
    'text': """
    递归思路 \n
- 当走到n层时可以选择再上一层或两层，直到仅剩1级或0级\n
- 打表记录n层的步数，避免重复计算\n
动态规划 \n
- 假设第i级台阶的爬楼梯方法数为dp[i]\n
- 要到达第i级台阶，可以从第i-1级台阶爬一级上来，或者从第i-2级台阶爬两级上来。因此，到达第i级台阶的方法数等于到达第i-1级台阶和第i-2级台阶方法数的和，即dp[i] = dp[i-1] + dp[i-2]\n
- dp[0] = 1（没有台阶时只有一种方法）dp[1] = 1（只有一级台阶时只有一种方法）\n
- 从i=2开始迭代计算dp[i]，直到计算出dp[n]，即到达第n级台阶的方法数。\n
    """,
    'writer': "测试用户",
    'review': []
}
e1 = essay(es1)

es2 = {
    'title': '排列的逆序数',
    'introduce':'逆序数 = 端点全在左边 + 端点全在右边 + 端点在两侧',
    'text': """
   long long  Mymerge(int l,int r){
    if(l>=r) return 0;//已经一个数字

    int mid=(l+r)/2;

    long long result = 0;

    result += Mymerge(l,mid) + Mymerge(mid+1,r);
//此时左右两侧均有序
    int k=0,i=l,j=mid+1;
    while(i <= mid && j <= r){
        if(num[i]>num[j]){
            temp[k++] = num[j++];
//            i - mid的数字与num[j]均为逆序
//			 计算后去除num[j],所以根据j算
            result += mid + 1 -i;
        }else{
//            正常
            temp[k++] = num[i++];
        }
    }
    while(i<=mid)temp[k++]=num[i++];
    while(j<=r)temp[k++]=num[j++];
    for (int i=l,k=0;i<=r;i++,k++){
        num[i]=temp[k];
    }
    return result;
}
""",
    'writer': "测试用户",
    'review': []
}
e2 = essay(es2)
