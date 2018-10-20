import glob
from PIL import Image

NOTHING = ''
SPACE = ' '
BREAK_LINE = '\n'

BASE_TEMPLATE = '''
<link href="../canvas.css" rel="stylesheet" />
%(table)s
%(table)s
<script>
  setInterval(() => {
    for (let i = 0; i < 100; i++) {
      const tds = document.querySelectorAll('td');
      const index = Math.floor(Math.random() * tds.length);
      const td = tds[index];
      td.parentElement.removeChild(td);
    }
  }, 100)
</script>
'''

def export_html(path, image):
  width = image.width
  height = image.height

  table = [
    '''
    <table align="center" cellspacing="0">
    '''
  ]

  for x in range(width):
    table.append(
      '''
      <tr>
      '''
    )

    for y in range(height):
      coords = (x, y)
      [r, g, b, a] = image.getpixel(coords)
      table.append(
        '''
          <td style="background: rgba({r}, {g}, {b}, {a});">
            
          </td>
        '''.format(
          r=r,
          g=g,
          b=b,
          a=a,
        )
      )
    table.append(
      '''
      </tr>
      '''
    )

  table.append(
    '''
    </table>
    '''
  )

  with open(
    path
      .replace('will-be-processed', 'final')
      .replace('png', 'html'),
    'w'
  ) as file:
    file.write(
      BASE_TEMPLATE % {
        'table': NOTHING.join(table)
      }
    )


def main():
  multipier = 0.1

  for path in glob.glob('will-be-processed/*.png'):
    image = Image.open(path)

    print(image.width)

    image.thumbnail((
      int(image.width * multipier),
      int(image.height * multipier)
    ))

    export_html(path, image.rotate(90))

if __name__ == '__main__':
  main()
