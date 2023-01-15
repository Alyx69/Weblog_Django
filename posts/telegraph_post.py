from telegraph import Telegraph
from .models import Posts

telegraph = Telegraph()
telegraph.create_account(short_name='Alyx69')

response = telegraph.create_page(
    f'{Posts.title}',
    html_content=f'<p>{Posts.body} \n response["url"]</p>'
)
print(response['url'])