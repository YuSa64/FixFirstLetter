bl_info = {
    "name": "Fix Shapekey First Letter",
    "author": "YuSa64",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > YuSa64",
    "description": "Change all first letters of shape key names to lowercase",
    "category": "3D View",
}

import bpy

# 쉐이프키 이름 변경 기능을 실행하는 Operator 정의
class OBJECT_OT_lowercase_shapekey_names(bpy.types.Operator):
    bl_idname = "object.lowercase_shapekey_names"
    bl_label = "Lowercase Shape Key Names"
    bl_description = "Make the first letter of all shape key names lowercase"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        obj = context.active_object
        if obj.data.shape_keys:
            for key_block in obj.data.shape_keys.key_blocks:
                name = key_block.name
                if name:  # 이름이 있는 경우
                    new_name = name[0].lower() + name[1:]
                    key_block.name = new_name
                    self.report({'INFO'}, f'Changed "{name}" to "{new_name}"')
        else:
            self.report({'WARNING'}, "This object has no shape keys.")
        return {'FINISHED'}

# 사이드바에 패널 추가
class VIEW3D_PT_lowercase_shapekey_panel(bpy.types.Panel):
    bl_label = "Shape Key Tools"
    bl_idname = "VIEW3D_PT_lowercase_shapekey_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "YuSa64"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_lowercase_shapekey_names.bl_idname)

# Blender에 클래스를 등록하고, 메뉴에 기능을 추가
def register():
    bpy.utils.register_class(OBJECT_OT_lowercase_shapekey_names)
    bpy.utils.register_class(VIEW3D_PT_lowercase_shapekey_panel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_lowercase_shapekey_names)
    bpy.utils.unregister_class(VIEW3D_PT_lowercase_shapekey_panel)

if __name__ == "__main__":
    register()
