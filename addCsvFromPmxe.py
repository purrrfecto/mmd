import bpy
import csv

def read_some_data(context, filepath, use_some_setting, codec_type):
    print("running read_some_data...")
    #print(codec_type)
    #shift-JIS = cp932, otherwise utf-8
    with open(filepath, 'r', encoding=codec_type) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(csvreader)
        print(', '.join(header))
        if "Body" in header[0]:
            print("rigid body csv")
        elif "Joint" in header[0]:
            print("joint csv")
        #for row in csvreader:
            #print(', '.join(row))
            
            
    #Joint
    #;Joint, Joint名, Joint名(英), 剛体名A, 剛体名B, Jointタイプ(0:ﾊﾞﾈ付6DOF/1:6DOF/2:P2P/3:ConeTwist/4:Slider/5:Hinge/), 位 置_x, 位置_y, 位置_z, 回転_x[deg], 回転_y[deg], 回転_z[deg], 移動下限_x, 移動下限_y, 移動下限_z, 移動上限_x, 移動上限_y, 移動上限_z, 回転下限_x[deg], 回転下限_y[deg], 回転下限_z[deg], 回転上限_x[deg], 回転上限_y[deg], 回転上限_z[deg], バネ 定数-移動_x, バネ定数-移動_y, バネ定数-移動_z, バネ定数-回転_x, バネ定数-回転_y, バネ定数-回転_z
    #Rigidbody
    #;Body,剛体名,剛体名(英),関連ボーン名,剛体タイプ(0:Bone/1:物理演算/2:物理演算+ボーン追従),グループ(0~15),非衝突グループ文字列(ex:1 2 3 4),形状(0:球/1:箱/2:カプセル),サイズ_x,サイズ_y,サイズ_z,位置_x,位置_y,位置_z,回転_x[deg],回転_y[deg],回転_z[deg],質量,移動減衰,回転減衰,反発力,摩擦力
    # Joint or rigidbody
    # find name
    # create/update object
    # createRigidBody / createJoint
      

    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportSomeData(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Some Data"

    # ImportHelper mixin class uses this
    filename_ext = ".csv"

    filter_glob: StringProperty(
        default="*.csv",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )

    type: EnumProperty(
        name="Choose CSV codec",
        description="Choose the csv codec of your file. Default is shift-JIS for japanese version user",
        items=(
            ('cp932', "shift_JIS", "Japanese non-unicode (default)"),
            ('utf-8', "UTF-8", "UTF-8"),
        ),
        default='cp932',
    )

    def execute(self, context):
        return read_some_data(context, self.filepath, self.use_setting, self.type)


# Only needed if you want to add into a dynamic menu.
def menu_func_import(self, context):
    self.layout.operator(ImportSomeData.bl_idname, text="Text Import Operator")


# Register and add to the "file selector" menu (required to use F3 search "Text Import Operator" for quick access).
def register():
    bpy.utils.register_class(ImportSomeData)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportSomeData)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
