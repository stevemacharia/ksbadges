from django.contrib import admin
from .models import ProductImage
from .models import Product

admin.site.register(Product)

admin.site.register(ProductImage)














# from .models import Post, PostImage

# class PostImageAdmin(admin.StackedInline):
#     model = PostImage

# admin.site.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]

#     class Meta:
#          model = Post

# admin.site.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass























# from django.contrib import admin
# from .models import ProductImage
# from .models import Product


# Post=Product
# PostImage= ProductImage

# class PostImageAdmin(admin.StackedInline):
#     model = PostImage

# admin.site.register(Post)
# class PostAdmin(admin.ModelAdmin):
#    inlines = [PostImageAdmin]

# admin.site.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass
  
















# class PostImageAdmin(admin.StackedInline): 
#     model = ProductImage

# admin.site.register(Product)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin] 
# class Meta:model = Product




# admin.site.register(ProductImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

# # /////

# from django.contrib import admin
# from .models import Case, CaseFile

# class CaseFileAdmin(admin.StackedInline):
#     model = CaseFile

# @admin.register(Case)
# class CaseAdmin(admin.ModelAdmin):
#     inlines = [CaseFileAdmin]

# @admin.register(CaseFile)
# class CaseFileAdmin(admin.ModelAdmin):
#     pass





# Post=Product
# PostImage= ProductImage


# class PostImageAdmin(admin.StackedInline): model = PostImage

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):inlines = [PostImageAdmin] 
# class Meta:model = Post

# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):pass
