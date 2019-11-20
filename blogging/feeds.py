# from django.contrib.syndication.views import Feed
# from django.urls import reverse

# from blogging.models import Post

# class LatestEntriesFeed(Feed):
#     title = "Latest Posts"
#     link = "/latestposts/"
#     description = "Top 10 most recent posts"

#     def items(self):
#         return Post.objects.order_by('published_date')

#     def item_title(self, item):
#         return item.title

#     def item_description(self, item):
#         return item.text

#     def item_link(self, item):
#         return reverse('posts/', args=[item.pk])