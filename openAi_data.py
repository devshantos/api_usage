import openai

openai.api_key = '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'
User_input = input("Enter your command: ")
'''response = openai.Completion.create(
  model="text-davinci-003",
  prompt= User_input,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)'''
Content = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'Write content for {User_input}',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
History = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'Write history of {User_input}',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
Place = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'Write Most beautiful place in {User_input}',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
Liberation = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'Write for Liberation war for {User_input}',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
Population = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'Write Population of and area {User_input}',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
Conclusion = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'Write for conclusion for {User_input}',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
Content = Content.get('choices')[0].get('text')
History = History.get('choices')[0].get('text')
Place = Place.get('choices')[0].get('text')
Population = Population.get('choices')[0].get('text')
Conclusion = Conclusion.get('choices')[0].get('text')
Liberation = Liberation.get('choices')[0].get('text')
all_data = f'<!-- wp:heading {"level":3} --> <h3> <strong> Introduction </strong></h3> <!-- /wp:heading --> <!-- wp:paragraph --><p>{Content}</p><!-- /wp:paragraph --><!-- wp:heading {"level":3} --><h3><strong>History</strong></h3><!-- /wp:heading --><!-- wp:paragraph --><p>{History}</p><!-- /wp:paragraph --><!-- wp:heading {"level":3} --><h3><strong>Population</strong></h3><!-- /wp:heading --><!-- wp:paragraph --><p>{Population}</p><!-- /wp:paragraph --><!-- wp:heading {"level":3} --><h3><strong>Liberation</strong></h3><!-- /wp:heading --><!-- wp:paragraph --><p>{Liberation}</p><!-- /wp:paragraph --><!-- wp:heading {"level":3} --><h3><strong>Place</strong></h3><!-- /wp:heading --><!-- wp:paragraph --><p>{Place}</p><!-- /wp:paragraph --><!-- wp:heading {"level":3} --><h3><strong>Conclusion</strong></h3><!-- /wp:heading --><!-- wp:paragraph --><p>{Conclusion}</p><!-- /wp:paragraph -->'
print(all_data)
