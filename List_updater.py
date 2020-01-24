def list_updater(vx, vk, scale):
    temp = [vx[0]]
    for i in range(1, len(vx)):
        temp.append(vx[i] + scale * vk[i])
    return temp
