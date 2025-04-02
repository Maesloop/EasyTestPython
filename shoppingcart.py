class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount_code = None
        
    def add_item(self, item_name, price, quantity=1):
        """Přidá položku do košíku nebo aktualizuje množství, pokud položka již existuje."""
        if not isinstance(item_name, str) or not item_name.strip():
            raise ValueError("Název položky musí být neprázdný řetězec")
        
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Cena musí být kladné číslo")
            
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Množství musí být kladné celé číslo")
            
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
        
        return True
        
    def remove_item(self, item_name, quantity=None):
        """Odstraní položku z košíku nebo sníží její množství."""
        if item_name not in self.items:
            return False
            
        if quantity is None or quantity >= self.items[item_name]['quantity']:
            del self.items[item_name]
        else:
            self.items[item_name]['quantity'] -= quantity
            
        return True
        
    def get_total(self):
        """Vypočítá celkovou cenu nákupu včetně případné slevy."""
        subtotal = sum(item['price'] * item['quantity'] for item in self.items.values())
        
        # Aplikace slevy, pokud je zadán slevový kód
        if self.discount_code == "SLEVA10":
            discount = subtotal * 0.1
            return subtotal - discount
        elif self.discount_code == "SLEVA20":
            discount = subtotal * 0.2
            return subtotal - discount
            
        return subtotal
        
    def apply_discount(self, code):
        """Aplikuje slevový kód na nákup."""
        valid_codes = ["SLEVA10", "SLEVA20"]
        
        if code in valid_codes:
            self.discount_code = code
            return True
        return False
        
    def clear_cart(self):
        """Vymaže obsah košíku."""
        self.items = {}
        self.discount_code = None
        return True
        
    def get_item_count(self):
        """Vrátí celkový počet položek v košíku."""
        if not self.items:
            return 0
        return sum(item['quantity'] for item in self.items.values())
        
    def update_item_price(self, item_name, new_price):
        """Aktualizuje cenu položky v košíku."""
        if item_name not in self.items:
            return False
            
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError("Nová cena musí být kladné číslo")
            
        self.items[item_name]['price'] = new_price
        return True
    
    def get_cart_contents(self):
        """Vrátí obsah košíku v čitelném formátu pro testování."""
        contents = []
        for item_name, details in self.items.items():
            contents.append(f"{item_name}: {details['quantity']} ks × {details['price']} Kč")
        return contents