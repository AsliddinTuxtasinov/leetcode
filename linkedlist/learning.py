class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # Bu method headni qaytarish uchun.
    @property
    def get_head(self) -> any:
        return self.head
    
    # Linked List bo'shmi yo'qmi tekshirish uchun method
    @property
    def is_empty(self) -> bool:
        return self.get_head is None
    
    # Linked Listdagi barcha nodelarni bitta oddiy list qilib chiqarish uchun.
    @property
    def get_all_nodes_value(self) -> list:
        result = list()
        
        # Agar head None bo'lsa [] qaytarsin.
        if self.is_empty:
            return result
        
        # Agar unday bo'lmasa demak iteratsiya qilib har bir nodeni datasi listga qo'shadi.
        current_node = self.head
        while current_node.next:
            result.append(current_node.value)
            current_node = current_node.next
        
        return result
    
    # Biz self.head ga qiymat qo'shish uchun append yaratdik.
    def append(self, value: any) -> None:
        # Birinchi bo'lib Node classidan yangi object yaratib olamiz.
        new_node = Node(value)
    
        # Endi esa linkedlistimiz bo'sh emasligini tekshirishimiz kerak.
        # Buning uchun self.headni tekshirish kifoya. Agar u None bo'lsa linked list bo'sh degani.
        if self.is_empty:
            self.head = new_node
            return 
        
        # Agar linkedlistimizda nodelar bo'lsa, demak biz oxirgi nodeni topishimiz kerak.
        # Oxirgi nodeni topish uchun qaysi nodeni nexti None ekanligni aniqlashmiz kerak.
        # Buning uchun self.head dan boshlab oxirgi nodegacha iteratsiya qilamiz.
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        # Demak last_node oxirgi elementni topdi. Uni nexti hozircha None.
        # Yangi element esa uni nextiga tushishi kerak.
        last_node.next = new_node
    
    # Bu method berilgan qiymatni linkedlistni boshiga qo'shadi ya'ni headga.
    def insert(self, value: any) -> None:
        new_head_node = Node(value)
        
        # Avval linked listni tekshiramiz va head bo'lmasa headga qo'shamiz
        if self.is_empty:
            self.head=new_head_node
            return
        
        # Head bo'lsa demak yangi elementni nextini headga qaratamiz.
        new_head_node.next = self.head
        
        # va new_node ni esa head deb tayinlaymiz.
        self.head = new_head_node
    
    # Biror qiymatni qidirish uchun ishlatiladi agar bo'lsa True bo'lmasa False qaytaradi.
    def search(self, value: any) -> bool:
        
        # Agar Linked List bo'sh bo'lsa None qaytarishi kerak qidirmasdan.
        if self.is_empty:
            return False
        
        # Agar qiymatlar bo'lsa, iteratsiya qilib ularni valuesi tekshiriladi.
        current_node = self.get_head
        while current_node.next:
            if current_node.value == value:
                return True
            
            current_node = current_node.next
        
        return False


 
my_list = LinkedList()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list.get_all_nodes_value)
print(my_list.search(value=6))