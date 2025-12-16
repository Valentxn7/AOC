class junction:
    from box_class import box
    def __init__(self):
        from box_class import box
        self.box_list: list[box] = list()

    def add_box(self, box: box):
        self.box_list.append(box)

    def taille(self):
        return len(self.box_list)

    def merge(self, other_junction):
        for box in other_junction.box_list:
            box.junction = self
        self.box_list = self.box_list + other_junction.box_list

    def __repr__(self):
        return f"<Junction {self.box_list=}>"