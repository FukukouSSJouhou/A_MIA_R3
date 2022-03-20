class FPCallbackFaceSelector:
    def __init__(self, callback):
        """
        constructor

        :param callback: callback method
        """
        self.callback = callback

    def execute(self, frame, front_face_list,fp_selector):
        """
        execute callback

        :param frame: frame object
        :param front_face_list: facelist
        :param fp_selector: target selector
        """
        self.callback(frame, front_face_list,fp_selector)
class FPCallbackFaceSelected:
    def __init__(self,callback):
        """
        constructor

        :param callback: callback obj
        """
        self.callback=callback
    def execute(self,target_img):
        """
        execute callback

        :param target_img: target image!!
        :return:none
        """

        self.callback(target_img)


