from os.path import join, dirname

import splicer
import splicer_arc
from splicer.servers.file_server import FileServer


def test_read():
  dataset = splicer.DataSet()

  dataset.add_server(FileServer(
    docs=dict(
      root_dir=join(dirname(__file__), 'data'),
      pattern="test.arc.gz",
      decode="application/x-arc"
    )
  ))

  docs  = dataset.frm('docs')
  doc = iter(docs).next()
