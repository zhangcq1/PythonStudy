'''
资源限制
时间限制：1.0s   内存限制：512.0MB
问题描述
　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，
    我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。

输入格式
　　输入仅包含两行，每行描述一个矩形。
　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不
    超过10^7的实数表示。

输出格式
　　输出仅包含一个实数，为交的面积，保留到小数后两位。
样例输入
1 1 3 3
2 2 4 4
样例输出
1.00
'''
def main():
    Rectangle1=list(map(float,input().strip().split(' ')))
    Rectangle2=list(map(float,input().strip().split(' ')))
    
    min1X=min(Rectangle1[0],Rectangle1[2])
    max1X=max(Rectangle1[0],Rectangle1[2])
    min1Y=min(Rectangle1[1],Rectangle1[3])
    max1Y=max(Rectangle1[1],Rectangle1[3])
    
    min2X=min(Rectangle2[0],Rectangle2[2])
    max2X=max(Rectangle2[0],Rectangle2[2])
    min2Y=min(Rectangle2[1],Rectangle2[3])
    max2Y=max(Rectangle2[1],Rectangle2[3])
    
    X1=max(min1X,min2X)
    X2=min(max1X,max2X)
    Y1=max(min1Y,min2Y)
    Y2=min(max1Y,max2Y)
    
    if X2-X1<0 or Y2-Y1<0:
        Area=0
        print('{:.2f}'.format(Area))
     
    else:
        Area=abs(Y2-Y1)*abs(X2-X1)
        print('{:.2f}'.format(Area))    
        
main()
