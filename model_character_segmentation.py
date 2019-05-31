
import cv2


class CharSegmentation:
    def charSegments(self,contours):
        k=[]
        for obj in contours:

            area = cv2.contourArea(obj)
            if area < 50:
                # if sample is too small, probably just artifact
                continue
            x, y, w, h = cv2.boundingRect(obj)#get bounded rectangle of contours
            k.append([y + h, x, y, w, h])
        return k

    def get_average_w_h(self,k):
        #get average width and height of list k of bounded rectangles
        ltr_width = 0
        ltr_height = 0
        if len(k)==0:
            return [ltr_width,ltr_height]
        for ltr in k:
            m, x, y, w, h = ltr
            ltr_width += w
            ltr_height += h

        # get average letter width and height
        ltr_width = ltr_width / len(k)
        ltr_height = ltr_height / len(k)
        return [ltr_width,ltr_height]

    def arrange(self,k):
        # this method is used to classify bounded rectangles into levels
        #sorted list with levels is returned

        k.sort()#sort the list
        if len(k)==0:#return empty list if list is empty
            return k

        j=1
        pm, px, py, pw, ph = k[0]
        k[0][0]=j#set levels according to y+h

        for i in range(1,len(k)):
            m, x, y, w, h = k[i]


            if pm-h/2.0 <= m <= pm+h/2.0:
                k[i][0]=j
                #if y+h is between +-h/2 then set same level
            else:
                #if not set j+1 level for y+h
                pm, px, py, pw, ph = k[i]
                j=j+1
                k[i][0]=j

        k.sort()
        return k


    def decode(self,pre):

        if len(pre)==0:
            return pre


        pre=self.arrange(pre) #set levels according to y+h

        ltr_width=self.get_average_w_h(pre)[0] #get average width of bounded rectangles in arranged list

        new=[]
        new.append(pre[0])
        x0=pre[0][1]
        y0=pre[0][0]
        for i in range(1,len(pre)):

            if (y0<pre[i][0]):
                #if level of one element is greater than level of previous element then "enter" is append
                new.append("enter")
            elif x0+ltr_width+5<pre[i][1] :
                #if left corner of bounded rectangle plus mean width+5 is less next bounded rectangle x value then
                #'space' is added
                new.append("space")
            x0=pre[i][1]
            y0=pre[i][0]
            # ltr_width=pre[i][3]
            new.append(pre[i])


        return new

    def textOrder(self,contours):
        k=self.charSegments(contours)
        new=self.decode(k)
        return new

