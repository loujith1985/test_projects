for core in range(1, 10):
    core_cloud_vlan = "50" + str(core)
    fw_cloud_vlan =  "60" + str(core)
    print("int vlan50" + str(core))
    print("description RT_transit_CC_CLOUD0", core, sep='')
    print("mtu 9000")
    print("vrf CC-CLOUD0", core, sep='')
    print("ip address 100.65.4.4/28 \n")


for core in range(10, 51):
    core_cloud_vlan = "5" + str(core)
    fw_cloud_vlan =  "6" + str(core)
    print("int vlan5" + str(core))
    print("description RT_transit_CC_CLOUD", core, sep='')
    print("mtu 9000")
    print("vrf CC-CLOUD", core, sep='')
    print("ip address 100.65.4.4/28 \n")


third_oct = 0
fourth_oct = 20
mask = "/28"
for fw in range(1, 51):
    if fw < 10:
        fw_cloud_vlan =  "60" + str(fw)
        print("int vlan60" + str(fw))
        print("description FW-EBGP-CC-CLOUD0" + str(fw) + "_60" + str(fw))
        print("mtu 9214")
        print("vrf CC-CLOUD0", fw, sep='')
        print("ip address 100.65." + str(third_oct) + "." + str(fourth_oct) + mask)
        print("\n")

    else:
        fw_cloud_vlan =  "6" + str(fw)
        print("int vlan6" + str(fw))
        print("description FW-EBGP-CC-CLOUD" + str(fw) + "_6" + str(fw))
        print("mtu 9214")
        print("vrf CC-CLOUD", fw, sep='')
        print("ip address 100.65." + str(third_oct) + "." + str(fourth_oct), mask, sep='')
        print("\n")

    if fourth_oct == 244:
        third_oct +=1
        fourth_oct = 4
    else:
        fourth_oct += 16
###Comment Line added##
