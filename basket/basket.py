from decimal import Decimal
from courses.models import Course


class Basket:
    """ Basket class for handling various functions """

    # Initialise basket or create empty one if not in session 
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket')

        if not basket:
            basket = self.session['basket'] = {}
        self.basket = basket

    # Add item to basket
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

    # Remove item from basket
    def remove(self, course):
        course_id = str(course.id)

        if course_id in self.basket:
            del self.basket[course_id]
            self.save()

    # 
    def __iter__(self):
        course_ids = self.basket.keys()
        courses = Course.objects.filter(id__in=course_ids)

        for course in courses:
            self.basket[str(course.id)]['course'] = course

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']
            yield item

    # Get total price of basket items
    def basket_total(self):
        total = 0  

        for item in self.basket.values():  
            total += Decimal(item['price'])  
        return total 
    
    # Save basket
    def save(self):
        self.session.modified = True

    # Get number of items in basket
    def __len__(self):
        return len(self.basket)
    
    # Clear the basket contents
    def clear(self):
        del self.session['basket']
        self.save()