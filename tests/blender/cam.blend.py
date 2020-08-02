import bpy
from blendtorch import btb

def main():
    btargs, remainder = btb.parse_blendtorch_args()

    cube = bpy.data.objects['Cube']
    ortho = btb.Camera(bpy.data.objects['CamOrtho'])
    proj = btb.Camera(bpy.data.objects['CamProj'])
    
    xyz = btb.utils.world_coordinates(cube)
    
    ortho_ndc = ortho.world_to_ndc(xyz)
    ortho_pix = ortho.ndc_to_pixel(ortho_ndc, origin='upper-left')
    ortho_z = ortho.ndc_to_linear_depth(ortho_ndc)

    proj_ndc = proj.world_to_ndc(xyz)
    proj_pix = proj.ndc_to_pixel(proj_ndc, origin='upper-left')
    proj_z = proj.ndc_to_linear_depth(proj_ndc)

    pub = btb.DataPublisher(btargs.btsockets['DATA'], btargs.btid, lingerms=5000)
    pub.publish(ortho_xy=ortho_pix, ortho_z=ortho_z, proj_xy=proj_pix, proj_z=proj_z)


main()