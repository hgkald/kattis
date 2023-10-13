
def main(): 
    h, w, n = [int(x) for x in input().split()]
    bricks = [int(x) for x in input().split()]

    for height in range(h):
        width = 0
        while width < w: 
            width += bricks.pop(0)
            if width > w: 
                print("NO")
                return
    print("YES")

if __name__ == '__main__': 
    main()
