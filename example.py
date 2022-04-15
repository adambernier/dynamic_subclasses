# this is a test, this is only a test 

def modified_operator(the_operator):
    the_operator_class_str = type(the_operator).__name__
    fs = frozenset(["TheOperator",])
    if the_operator_class_str in fs:
        print('ok')
        the_operator_class = globals()[the_operator_class_str]
        modified_operator_instance = make_modified_operator_class(
                the_operator_class, the_operator,
        )
        return modified_operator_instance


def make_modified_operator_class(base, original_operator):
    kwargs = original_operator.__dict__
    
    
    class ModifiedOperator(base):
        def __init__(self, **kwargs):
            # self.a = kwargs.get("a")
            kwargs.pop('input_data')
            kwargs.pop('output_data')
            super().__init__(**kwargs)
            # explicitly done because these were created by __init__()
            del self.input_data 
            del self.output_data 
        def testing(self):
            try:
                print(self.input_data)
                print('something odd happened')
            except AttributeError:
                print('good to go')
            
            
    return ModifiedOperator(**kwargs)


class TheOperator(object):
    def __init__(self, a):
        self.a = 'test'
        self.input_data = {}
        self.output_data = {}
    def super_method(self):
        print("super method is accessible!")
    

if __name__ == '__main__':
    test_operator = TheOperator('a')
    modified_operator = modified_operator(test_operator)
    modified_operator.testing()
    modified_operator.super_method()
