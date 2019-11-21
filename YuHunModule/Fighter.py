import logging
import time

from CommonUtil import ImgPath, CommonPosition
from CommonUtil.GlobalProperty import GlobalProperty
from CommonUtil.Logger import Logger
from ImageProcessModule.GameControl import GameControl
from YuHunModule.State import State


class Fighter:
    def __init__(self,name,hwnd):
        """
        初始化
        :param name: 司机或者乘客
        :param hwnd: 绑定的窗体句柄
        """
        self.name=name
        self.hwnd = hwnd
        # 控制子线程退出的变量
        self.run = State()
        self.game_control = GameControl(hwnd=hwnd, run=self.run, quit_game_enable=True)

    def click_until(self, tag: str, img_path: str, pos: tuple, pos_end: tuple = None, appear: bool = True):
        """
        不断点击pos坐标，直到图片消失或者出现
        :param tag: 出现或消失的图像tag
        :param img_path: 图像路径
        :param pos: 左上角位置
        :param pos_end: 右下角位置
        :param appear: True为出现，False为消失
        :return:
        """
        start_time = time.time()
        while time.time() - start_time <= GlobalProperty.max_no_response_time and self.run.is_running():
            result = self.game_control.find_game_img(img_path)
            # 如果是判断消失的话,要取反
            if appear is False:
                result = not result
            if result:
                logging.info('{}点击{}成功'.format(self.name,tag))
                self.yys.mouse_click_bg(pos, None)
                return True
        logging.warning('{}点击{}失败'.format(self.name,tag))

        # 提醒玩家点击失败，并在5s后退出
        self.yys.activate_window()
        time.sleep(5)
        self.yys.quit_game()
        return False

    def wait_fight_end(self):
        """
        等待御魂副本战斗结束
        :return:
        """
        logging.info('{}:检测是战斗是否结束'.format(self.name))
        self.game_control.wait_game_img(img_path=ImgPath.GetImgFilePath()+ImgPath.JIE_SHU,max_time=GlobalProperty.max_no_response_time)
        logging.info('{}:战斗已经否结束'.format(self.name))