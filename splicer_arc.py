from __future__ import absolute_import

from gzip import GzipFile


import warc

from splicer import Schema, Relation
from splicer.codecs import decodes

@decodes('application/x-arc')
def input_stream(stream):
  arc = warc.ARCFile(fileobj=GzipFile(fileobj=stream))

  schema = Schema([
    dict(name='url',          type='STRING'), 
    dict(name='checksum',     type='STRING'), 
    dict(name='filename',     type='STRING'),
    dict(name='length',       type='STRING'),
    dict(name='location',     type='STRING'),
    dict(name='content_type', type='STRING'),
    dict(name='offset',       type='STRING'),
    dict(name='date',         type='DATETIME'),
    dict(name='ip_address',   type='STRING'),
    dict(name='result_code',  type='INTEGER'),
    dict(name='payload',      type='STRING'),
  ])

  headers = [f.name for f in schema.fields[:-1]]

  def make_row(doc):
    row = [doc.header[h] for h in headers]
    row.append(doc.payload.decode('ascii', 'ignore'))
    return row

  return Relation(
    schema,
    (
      make_row(row)
      for row in arc
    )
  )