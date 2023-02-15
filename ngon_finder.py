bl_info = {
    "name": "NGon Finder",
    "author": "eddygordo",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "description": "Maya is Bug.",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}

import bpy
import bmesh

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "NGon Finder"
    bl_idname = "OBJECT_PT_NGF"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NGon Finder"

    def draw(self, context):
        row = self.layout.row()
        row.operator("object.simple_operator")

        
class SimpleOperator(bpy.types.Operator):
    """Find NGon Operator"""
    bl_idname = "object.ngf_operator"
    bl_label = "Find"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')

        # Get the active mesh
        obj = bpy.context.edit_object
        me = obj.data


        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(me)

        for face in bm.faces:
            if len(face.verts) == 4:
                face.select_set(False)
            else:
                face.select_set(True)

        # Show the updates in the viewport
        # and recalculate n-gon tessellation.
        bmesh.update_edit_mesh(me)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(NGFPanel)
    bpy.utils.register_class(NGFOperator)


def unregister():
    bpy.utils.unregister_class(NGFPanel)
    bpy.utils.unregister_class(NGFOperator)


if __name__ == "__main__":
    register()
