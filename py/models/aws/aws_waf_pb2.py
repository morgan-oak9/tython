# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aws/aws_waf.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oak9.tython.models.shared import shared_pb2 as shared_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ws/aws_waf.proto\x12\x13oak9.tython.aws.waf\x1a\x13shared/shared.proto\"o\n\x18\x42yteMatchSetFieldToMatch\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\x8d\x02\n\x1a\x42yteMatchSetByteMatchTuple\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x45\n\x0e\x66ield_to_match\x18\x02 \x01(\x0b\x32-.oak9.tython.aws.waf.ByteMatchSetFieldToMatch\x12\x1d\n\x15positional_constraint\x18\x03 \x01(\t\x12\x15\n\rtarget_string\x18\x04 \x01(\t\x12\x1c\n\x14target_string_base64\x18\x05 \x01(\t\x12\x1b\n\x13text_transformation\x18\x06 \x01(\t\"\xa1\x01\n\x0c\x42yteMatchSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12J\n\x11\x62yte_match_tuples\x18\x02 \x03(\x0b\x32/.oak9.tython.aws.waf.ByteMatchSetByteMatchTuple\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x8f\x03\n\x03WAF\x12\x39\n\x0e\x62yte_match_set\x18\x01 \x03(\x0b\x32!.oak9.tython.aws.waf.ByteMatchSet\x12*\n\x06ip_set\x18\x02 \x03(\x0b\x32\x1a.oak9.tython.aws.waf.IPSet\x12\'\n\x04rule\x18\x03 \x03(\x0b\x32\x19.oak9.tython.aws.waf.Rule\x12\x43\n\x13size_constraint_set\x18\x04 \x03(\x0b\x32&.oak9.tython.aws.waf.SizeConstraintSet\x12J\n\x17sql_injection_match_set\x18\x05 \x03(\x0b\x32).oak9.tython.aws.waf.SqlInjectionMatchSet\x12.\n\tweb_a_c_l\x18\x06 \x01(\x0b\x32\x1b.oak9.tython.aws.waf.WebACL\x12\x37\n\rxss_match_set\x18\x07 \x03(\x0b\x32 .oak9.tython.aws.waf.XssMatchSet\"^\n\x14IPSetIPSetDescriptor\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\r\n\x05value\x18\x02 \x01(\t\"\x95\x01\n\x05IPSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x45\n\x12ip_set_descriptors\x18\x02 \x03(\x0b\x32).oak9.tython.aws.waf.IPSetIPSetDescriptor\x12\x0c\n\x04name\x18\x03 \x01(\t\"x\n\rRulePredicate\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0f\n\x07\x64\x61ta_id\x18\x02 \x01(\t\x12\x0f\n\x07negated\x18\x03 \x01(\x08\x12\x0c\n\x04type\x18\x04 \x01(\t\"\x9a\x01\n\x04Rule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x13\n\x0bmetric_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x36\n\npredicates\x18\x04 \x03(\x0b\x32\".oak9.tython.aws.waf.RulePredicate\"f\n\x1dSizeConstraintSetFieldToMatch\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\xfc\x01\n\x1fSizeConstraintSetSizeConstraint\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x1b\n\x13\x63omparison_operator\x18\x02 \x01(\t\x12J\n\x0e\x66ield_to_match\x18\x03 \x01(\x0b\x32\x32.oak9.tython.aws.waf.SizeConstraintSetFieldToMatch\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\x1b\n\x13text_transformation\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\"\xaa\x01\n\x11SizeConstraintSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12N\n\x10size_constraints\x18\x03 \x03(\x0b\x32\x34.oak9.tython.aws.waf.SizeConstraintSetSizeConstraint\"w\n SqlInjectionMatchSetFieldToMatch\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\xd1\x01\n*SqlInjectionMatchSetSqlInjectionMatchTuple\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12M\n\x0e\x66ield_to_match\x18\x02 \x01(\x0b\x32\x35.oak9.tython.aws.waf.SqlInjectionMatchSetFieldToMatch\x12\x1b\n\x13text_transformation\x18\x03 \x01(\t\"\xc2\x01\n\x14SqlInjectionMatchSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x63\n\x1asql_injection_match_tuples\x18\x03 \x03(\x0b\x32?.oak9.tython.aws.waf.SqlInjectionMatchSetSqlInjectionMatchTuple\"X\n\x0fWebACLWafAction\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04type\x18\x02 \x01(\t\"\xa7\x01\n\x13WebACLActivatedRule\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x34\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32$.oak9.tython.aws.waf.WebACLWafAction\x12\x10\n\x08priority\x18\x03 \x01(\x05\x12\x0f\n\x07rule_id\x18\x04 \x01(\t\"\xdb\x01\n\x06WebACL\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12<\n\x0e\x64\x65\x66\x61ult_action\x18\x02 \x01(\x0b\x32$.oak9.tython.aws.waf.WebACLWafAction\x12\x13\n\x0bmetric_name\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x37\n\x05rules\x18\x05 \x03(\x0b\x32(.oak9.tython.aws.waf.WebACLActivatedRule\"`\n\x17XssMatchSetFieldToMatch\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\xb6\x01\n\x18XssMatchSetXssMatchTuple\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x44\n\x0e\x66ield_to_match\x18\x02 \x01(\x0b\x32,.oak9.tython.aws.waf.XssMatchSetFieldToMatch\x12\x1b\n\x13text_transformation\x18\x03 \x01(\t\"\x9d\x01\n\x0bXssMatchSet\x12\x37\n\rresource_info\x18\x01 \x01(\x0b\x32 .oak9.tython.shared.ResourceInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\x12G\n\x10xss_match_tuples\x18\x03 \x03(\x0b\x32-.oak9.tython.aws.waf.XssMatchSetXssMatchTupleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aws.aws_waf_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BYTEMATCHSETFIELDTOMATCH._serialized_start=63
  _BYTEMATCHSETFIELDTOMATCH._serialized_end=174
  _BYTEMATCHSETBYTEMATCHTUPLE._serialized_start=177
  _BYTEMATCHSETBYTEMATCHTUPLE._serialized_end=446
  _BYTEMATCHSET._serialized_start=449
  _BYTEMATCHSET._serialized_end=610
  _WAF._serialized_start=613
  _WAF._serialized_end=1012
  _IPSETIPSETDESCRIPTOR._serialized_start=1014
  _IPSETIPSETDESCRIPTOR._serialized_end=1108
  _IPSET._serialized_start=1111
  _IPSET._serialized_end=1260
  _RULEPREDICATE._serialized_start=1262
  _RULEPREDICATE._serialized_end=1382
  _RULE._serialized_start=1385
  _RULE._serialized_end=1539
  _SIZECONSTRAINTSETFIELDTOMATCH._serialized_start=1541
  _SIZECONSTRAINTSETFIELDTOMATCH._serialized_end=1643
  _SIZECONSTRAINTSETSIZECONSTRAINT._serialized_start=1646
  _SIZECONSTRAINTSETSIZECONSTRAINT._serialized_end=1898
  _SIZECONSTRAINTSET._serialized_start=1901
  _SIZECONSTRAINTSET._serialized_end=2071
  _SQLINJECTIONMATCHSETFIELDTOMATCH._serialized_start=2073
  _SQLINJECTIONMATCHSETFIELDTOMATCH._serialized_end=2192
  _SQLINJECTIONMATCHSETSQLINJECTIONMATCHTUPLE._serialized_start=2195
  _SQLINJECTIONMATCHSETSQLINJECTIONMATCHTUPLE._serialized_end=2404
  _SQLINJECTIONMATCHSET._serialized_start=2407
  _SQLINJECTIONMATCHSET._serialized_end=2601
  _WEBACLWAFACTION._serialized_start=2603
  _WEBACLWAFACTION._serialized_end=2691
  _WEBACLACTIVATEDRULE._serialized_start=2694
  _WEBACLACTIVATEDRULE._serialized_end=2861
  _WEBACL._serialized_start=2864
  _WEBACL._serialized_end=3083
  _XSSMATCHSETFIELDTOMATCH._serialized_start=3085
  _XSSMATCHSETFIELDTOMATCH._serialized_end=3181
  _XSSMATCHSETXSSMATCHTUPLE._serialized_start=3184
  _XSSMATCHSETXSSMATCHTUPLE._serialized_end=3366
  _XSSMATCHSET._serialized_start=3369
  _XSSMATCHSET._serialized_end=3526
# @@protoc_insertion_point(module_scope)
