def create_phone_number(n):
    phone = n
    x = '('+str(phone[0])+str(phone[1])+str(phone[2])+') '+str(phone[3])+str(phone[4])+str(phone[5])+'-'+str(phone[6])+str(phone[7])+str(phone[8])+str(phone[9])
    return x


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])