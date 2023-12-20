import models import Athlete

AthleteSerializer = AthleteSerializerFactory(
    model = Athlete,
    fields=('name', 'sport', 'earnings', 'year'),
    many=True
)