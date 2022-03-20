class FPCallbackFaceSelector:
    def __init__(self, callback):
        """
        constructor

        :param callback: callback method
        """
        self.callback = callback

    def execute(self, frame, front_face_list,target_image):
        """
        execute callback

        :param frame: frame object
        :param front_face_list: facelist
        :param target_image: target image
        """
        self.callback(frame, front_face_list,target_image)
