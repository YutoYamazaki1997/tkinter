class Controller:
    def __init__(self, app, model, view):
        self.app = app
        self.model = model
        self.view = view

        self.view.right_btn["command"] = self.push_right_btn
        self.view.left_btn["command"] = self.push_left_btn

    def push_right_btn(self):
        self.view.create_right_frame()
        lambda: self.changePage(self.view.right_frame)

    def push_left_btn(self):
        print("L")

    def changePage(self, page):
        '''
        画面遷移用の関数
        '''
        page.tkraise()
