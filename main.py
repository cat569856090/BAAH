import sys
import os
# 将当前脚本所在目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

if __name__ in ["__main__", "__mp_main__"]:
    try:
        # config logging before all imports
        import logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')
        import base64
        import traceback
        from gui import BAAH_GUI
        from BAAH import BAAH_main
        from assets.Aris import aris_base64
        from modules.utils.MyConfig import config
        print("+"+"BAAH".center(80, "="), "+")
        print("||"+f"Version: {config.NOWVERSION}".center(80, " ")+"||")
        print("||"+"Bilibili: https://space.bilibili.com/7331920".center(80, " ")+"||")
        print("||"+"Github: https://github.com/sanmusen214/BAAH".center(80, " ")+"||")
        print("||" + "QQ群: 441069156".center(80, " ") + "||")
        print("||"+"".center(80, " ")+"||")
        print("+"+"".center(80, "=")+"+")
        # base64解码
        print(base64.b64decode(aris_base64).decode("utf-8"))
    

        # 不带GUI运行
        BAAH_main()
        # 带GUI运行
        # gui = BAAH_GUI(BAAH_main)
        # gui.runGUI()
    except Exception as e:
        # 打印完整的错误信息
        traceback.print_exc()
    input("按回车键退出BAAH:")
