class DexPrinter (object):
    def __init__(self,meta_verbose=False):
        self.meta_verbose = meta_verbose

    def max_attr(self,obj):
        return max([len(i[0]) for i in obj._fields_])
            
    def print_attr(self,attr,val,pad,size):
        msg = ' '*pad
        msg += attr + ':'
        msg += ' '* (size-len(msg)+pad+4)
        msg += str(val)

        print msg
        
    def print_label(self,msg,pad):
        print ' '*pad + msg + ':'
        
    def meta(self,obj,pad=0):
        if not self.meta_verbose: return

        self.print_label('Metadata',pad)
        
        size = self.max_attr(obj)
        pad += 2

        self.print_attr('corrupted',obj.corrupted,pad,size)
        self.print_attr('offset',hex(obj.offset),pad,size)

    def header(self,obj,pad=0):
        self.print_label("Header",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('magic',''.join(['%02x'%x for x in obj.magic]),pad,size)
        self.print_attr('checksum',obj.checksum,pad,size)
        self.print_attr('signature',''.join(['%02x'%x for x in obj.signature])
                        ,pad,size)
        self.print_attr('file_size',obj.file_size,pad,size)
        self.print_attr('header_size',obj.header_size,pad,size)
        self.print_attr('endian_tag',obj.endian_tag,pad,size)
        self.print_attr('link_size',obj.link_size,pad,size)
        self.print_attr('link_off',hex(obj.link_off),pad,size)
        self.print_attr('map_off',hex(obj.map_off),pad,size)
        self.print_attr('string_ids_size',obj.string_ids_size,pad,size)
        self.print_attr('string_ids_off',hex(obj.string_ids_off),pad,size)
        self.print_attr('type_ids_size',obj.type_ids_size,pad,size)
        self.print_attr('type_ids_off',hex(obj.type_ids_off),pad,size)
        self.print_attr('proto_ids_size',obj.proto_ids_size,pad,size)
        self.print_attr('proto_ids_off',hex(obj.proto_ids_off),pad,size)
        self.print_attr('field_ids_size',obj.field_ids_size,pad,size)
        self.print_attr('field_ids_off',hex(obj.field_ids_off),pad,size)
        self.print_attr('method_ids_size',obj.method_ids_size,pad,size)
        self.print_attr('method_ids_off',hex(obj.method_ids_off),pad,size)
        self.print_attr('class_defs_size',obj.class_defs_size,pad,size)
        self.print_attr('class_defs_off',hex(obj.class_defs_off),pad,size)
        self.print_attr('data_size',obj.data_size,pad,size)
        self.print_attr('data_off',hex(obj.data_off),pad,size)

    def stringid(self,obj,pad=0):
        self.print_label("StringId",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('string_data_off',hex(obj.string_data_off),pad,size)

    def stringdata(self,obj,pad=0):
        self.print_label("StringData",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('size',obj.size.uleb(),pad,size)
        self.print_attr('data',str(obj.data)[:obj.size.uleb()],pad,size)

    def typeid(self,obj,pad=0):
        self.print_label("TypeId",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('descriptor_idx',obj.descriptor_idx,pad,size)
    

    def protoid(self,obj,pad=0):
        self.print_label("ProtoId",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('shorty_idx',obj.shorty_idx,pad,size)
        self.print_attr('return_type_idx',obj.return_type_idx,pad,size)
        self.print_attr('parameters_off',obj.parameters_off,pad,size)


    def fieldid(self,obj,pad=0):
        self.print_label("FieldId",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('class_idx',obj.class_idx,pad,size)
        self.print_attr('type_idx',obj.type_idx,pad,size)
        self.print_attr('name_idx',obj.name_idx,pad,size)

    def methodid(self,obj,pad=0):
        self.print_label("MethodId",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('class_idx',obj.class_idx,pad,size)
        self.print_attr('proto_idx',obj.proto_idx,pad,size)
        self.print_attr('name_idx',obj.name_idx,pad,size)

    def classdef(self,obj,pad=0):
        self.print_label("ClassDef",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('class_idx',obj.class_idx,pad,size)
        self.print_attr('access_flags',obj.access_flags,pad,size)
        self.print_attr('superclass_idx',obj.superclass_idx,pad,size)
        self.print_attr('interfaces_off',obj.interfaces_off,pad,size)
        self.print_attr('source_file_idx',obj.source_file_idx,pad,size)
        self.print_attr('annotations_off',obj.annotations_off,pad,size)
        self.print_attr('class_data_off',obj.class_data_off,pad,size)
        self.print_attr('static_values_off',obj.static_values_off,pad,size)

    def encodedfield(self,obj,pad=0):
        self.print_label("EncodedField",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('field_idx_diff',obj.field_idx_diff.uleb(),pad,size)
        self.print_attr('access_flags',obj.access_flags.uleb(),pad,size)

    def encodedmethod(self,obj,pad=0):
        self.print_label("EncodedMethod",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('method_idx_diff',obj.method_idx_diff.uleb(),pad,size)
        self.print_attr('access_flags',obj.access_flags.uleb(),pad,size)
        self.print_attr('code_off',hex(obj.code_off.uleb()),pad,size)

    def classdata(self,obj,pad=0):
        self.print_label("ClassData",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('static_fields_size',obj.static_fields_size.uleb(),pad,size)
        self.print_attr('instance_fields_size',obj.instance_fields_size.uleb(),
                        pad,size)
        self.print_attr('direct_methods_size',obj.direct_methods_size.uleb(),pad,size)
        self.print_attr('virtual_methods_size',obj.virtual_methods_size.uleb(),
                        pad,size)

        self.print_label("static_fields",pad)
        for i in xrange(obj.static_fields_size.uleb()):
            self.encodedfield(obj.static_fields[i].contents,pad+2)

        self.print_label("instance_fields",pad)
        for i in xrange(obj.instance_fields_size.uleb()):
            self.encodedfield(obj.instance_fields[i].contents,pad+2)

        self.print_label("direct_methods",pad)
        for i in xrange(obj.direct_methods_size.uleb()):
            self.encodedmethod(obj.direct_methods[i].contents,pad+2)

        self.print_label("virtual_methods",pad)
        for i in xrange(obj.virtual_methods_size.uleb()):
            self.encodedmethod(obj.virtual_methods[i].contents,pad+2)

    def typeitem(self,obj,pad=0):
        self.print_label("TypeItem",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('type_idx',obj.type_idx,pad,size)

    def typelist(self,obj,pad=0):
        self.print_label("TypeList",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('size',obj.size,pad,size)

        for i in xrange(obj.size):
            self.typeitem(obj.list[i].contents,pad)

    def tryitem(self,obj,pad=0):
        self.print_label("TryItem",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('start_addr',hex(obj.start_addr),pad,size)
        self.print_attr('insns_count',obj.insns_count,pad,size)
        self.print_attr('handler_off',obj.handler_off,pad,size)

    def encodedtypeaddrpair(self,obj,pad=0):
        self.print_label("EncodedTypeAddrPair",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('type_idx',obj.type_idx.uleb(),pad,size)
        self.print_attr('addr',hex(obj.addr.uleb()),pad,size)

    def encodedcatchhandler(self,obj,pad=0):
        self.print_label("EncodedCatchHandler",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('size',obj.size.sleb(),pad,size)

        self.print_label('handlers',pad)
        for i in xrange(abs(obj.size.sleb())):
            self.encodedtypeaddrpair(obj.handlers[i].contents,pad)

        if obj.size.sleb() <= 0:
            self.print_attr('catch_all_addr',hex(obj.catch_all_addr.uleb()),pad,size)

    def encodedcatchhandlerlist(self,obj,pad=0):
        self.print_label("EncodedCatchHandlerList",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('size',obj.size.uleb(),pad,size)

        self.print_label('list',pad)
        for i in xrange(obj.size.uleb()):
            self.encodedcatchhandler(obj.list[i].contents,pad+2)

    def codeitem(self,obj,pad=0):
        self.print_label("CodeItem",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('registers_size',obj.registers_size,pad,size)
        self.print_attr('ins_size',obj.ins_size,pad,size)
        self.print_attr('outs_size',obj.outs_size,pad,size)
        self.print_attr('tries_size',obj.tries_size,pad,size)
        self.print_attr('debug_info_off',hex(obj.debug_info_off),pad,size)
        self.print_attr('insns_size',obj.insns_size,pad,size)

        self.print_label('insns',pad)
        line = ' '*(pad+2)
        for i in xrange(obj.insns_size):            
            line += '%04x' % obj.insns[i]

            if (len(line) % 60) == 0:
                print line
                line =' '*(pad+2)

        print line

        self.print_attr('padding',hex(obj.padding),pad,size)
        
        self.print_label('tries',pad)
        for i in xrange(obj.tries_size):
            self.tryitem(obj.tries[i].contents,pad+2)

        self.print_label('handlers',pad)
        if obj.tries_size > 0:
            self.encodedcatchhandlerlist(obj.handlers.contents,pad+2)

    def debuginfo(self,obj,pad=0):
        self.print_label("DebugInfo",pad)

        size = self.max_attr(obj)
        pad +=2

        self.meta(obj.meta,pad)

        self.print_attr('line_start',obj.line_start.uleb(),pad,size)
        self.print_attr('parameters_size',obj.parameters_size.uleb(),pad,size)

        self.print_label('parameter_names',pad)
        for i in xrange(obj.parameters_size.uleb()):
            print ' '*(pad+2) + '%d' % obj.parameter_names[i].ulebp1()

        self.print_label('state_machine',pad)
        line = ' '*(pad+2)
        i = 0
        while obj.state_machine[i] != 0x0:
            line += '%02x' % obj.state_machine[i]

            if (len(line) % 60) == 0:
                print line
                line =' '*(pad+2)

            i+=1

        line += '00'
        print line

    def mapitem(self,obj,pad=0):
        self.print_label("MapItem",pad)
        
        pad += 2

        self.meta(obj.meta,pad)
        
        size = self.max_attr(obj)

        self.print_attr('type',hex(obj.type),pad,size)
        self.print_attr('unused',obj.unused,pad,size)
        self.print_attr('size',obj.size,pad,size)
        self.print_attr('offset',obj.offset,pad,size)
        
    def maplist(self,obj,pad=0):
        self.print_label("MapList",pad)

        pad += 2

        self.meta(obj.meta,pad)

        self.print_attr("size",obj.size,pad,4)

        self.print_label('list',pad)
        for i in xrange(obj.size):
            self.mapitem(obj.list[i].contents,pad+2)

    def encodedvalue(self,obj,pad=0):
        self.print_label("EncodedValue",pad)

        pad += 2

        self.meta(obj.meta,pad)

        size = self.max_attr(obj)

        obj_type = (obj.argtype & 0x1f)        
        obj_arg = ((obj.argtype >> 5) & 0x7)
        
        self.print_attr('argtype',hex(obj.argtype),pad,size)

        self.print_attr('type',hex(obj_type),pad,size)
        self.print_attr('arg',obj_arg,pad,size)

        if obj_type == 0x0:
            self.print_attr('value',int(obj.value.contents),pad,size)
        elif obj_type in [0x2,0x3,0x4,0x6,0x10,0x11,0x17,0x18,0x19,0x1a,0x1b]:
            self.print_label('value',pad)
            data = ' '*(pad+2)
            for i in xrange(obj_arg+1):
                data += "%02x" % obj.value[i]
            print data
        elif obj_type == 0x1c:
            self.print_label('value',pad)
            self.encodedarray(obj.value.contents,pad+2)
        elif obj_type == 0x1d:
            self.print_label('value',pad)
            self.encodedannotation(obj.value.contents,pad+2)
        elif obj_type in [0x1e,0x1f]:
            self.print_label('value',pad)
        else:
            self.print_label('value',pad)
            print ' '*(pad+2) + 'Unknown'
        
    def encodedarray(self,obj,pad=0):
        self.print_label("EncodedArray",pad)

        pad += 2

        self.meta(obj.meta,pad)

        size = self.max_attr(obj)

        self.print_attr('size',obj.size.uleb(),pad,size)

        self.print_label('values',pad)
        for i in xrange(obj.size.uleb()):
            self.encodedvalue(obj.values[i].contents,pad+2)
        
    def annotationelement(self,obj,pad=0):
        self.print_label("AnnotationElement",pad)

        pad += 2

        self.meta(obj.meta,pad)

        size = self.max_attr(obj)

        self.print_attr('name_idx',obj.name_idx.uleb(),pad,size)
        self.print_label('value')
        self.encodedvalue(obj.value.contents,pad+2)

    def encodedannotation(self,obj,pad=0):
        self.print_label("EncodedAnnotation",pad)

        pad += 2

        self.meta(obj.meta,pad)

        size = self.max_attr(obj)

        self.print_attr('type_idx',obj.type_idx.uleb(),pad,size)
        self.print_attr('size',obj.size.uleb(),pad,size)

        self.print_label('elements',pad)
        for i in xrange(obj.size.uleb()):
            self.annotationelement(obj.elements[i].contents,pad+2)
