import scripts
print("=>")
vlans = [10,20,30,99]
vlan_dict = {}
for vlan_id in vlans:
    vlan_dict[f"vlan_id_{vlan_id}"]=vlan_id
print(vlan_dict)
print("<=")