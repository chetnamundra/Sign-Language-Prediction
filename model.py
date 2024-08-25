def nearest(p):

    if p[8][1]<p[6][1] and p[20][1]<p[17][1] and p[12][1]>p[10][1] and p[16][1]>p[14][1]:
        return 'I Love You'
    elif p[8][1]<p[6][1] and p[20][1]<p[17][1] and p[12][1]<p[10][1] and p[16][1]<p[14][1]:
            if p[4][0]<p[17][0]:
                return 'Hello'
            else:
                return 'Thank You'
    else:
        
        if p[4][1]>p[0][1] and p[13][0]>p[1][0]:
            return 'Yes'
        elif p[4][1]>p[0][1] and p[13][0]<p[1][0]:
                return 'No'
        elif p[13][0]<p[1][0] and p[4][1]<p[0][1]:
            return 'Yes'
        elif p[20][0]<p[18][0] and p[16][0]<p[14][0]:
                return 'Good Bye'
        elif p[20][0]>p[18][0] and p[16][0]>p[14][0]:
                return 'No'
        return ''
