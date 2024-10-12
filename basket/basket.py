from decimal import Decimal
from courses.models import Course


class Basket:
    """ Create empty basket """
    def __init__(self, request):
        # Get instance of request session
        self.session = request.session

        # Get value of basket
        basket = self.session.get('basket')

        # Check basket
        if not basket:
            # If basket has no value create empty basket
            basket = self.session['basket'] = {}
        self.basket = basket


    def add(self, course):
        course_id = str(course.id)

        if course_id not in self.basket:
            self.basket[course_id] = {
                'course' : course_id,
                'title' : str(course.title),
                'description' : str(course.description),
                'quantity' : 1,
                'price' : str(course.price),
                }
        self.save()


    def remove(self, course):
        course_id = str(course.id)

        if course_id in self.basket:
            del self.basket[course_id]
            self.save()


    def __iter__(self):
        course_ids = self.basket.keys()
        courses = Course.objects.filter(id__in=course_ids)

        for course in courses:
            self.basket[str(course.id)]['course'] = course

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']
            yield item


    def basket_total(self):
        total = 0  

        for item in self.basket.values():  
            total += Decimal(item['price'])  
        return total 
    

    def save(self):
        self.session.modified = True


    def __len__(self):
        return len(self.basket)
    

    def clear(self):
        del self.session['basket']
        self.save()

