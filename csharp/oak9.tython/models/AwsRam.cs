// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: aws/aws_ram.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Aws.Ram {

  /// <summary>Holder for reflection information generated from aws/aws_ram.proto</summary>
  public static partial class AwsRamReflection {

    #region Descriptor
    /// <summary>File descriptor for aws/aws_ram.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static AwsRamReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChFhd3MvYXdzX3JhbS5wcm90bxITb2FrOS50eXRob24uYXdzLnJhbRoTc2hh",
            "cmVkL3NoYXJlZC5wcm90byKNAgoNUmVzb3VyY2VTaGFyZRI3Cg1yZXNvdXJj",
            "ZV9pbmZvGAEgASgLMiAub2FrOS50eXRob24uc2hhcmVkLlJlc291cmNlSW5m",
            "bxISCgpwcmluY2lwYWxzGAIgAygJEiEKGWFsbG93X2V4dGVybmFsX3ByaW5j",
            "aXBhbHMYAyABKAgSFQoNcmVzb3VyY2VfYXJucxgEIAMoCRI6CgR0YWdzGAUg",
            "AygLMiwub2FrOS50eXRob24uYXdzLnJhbS5SZXNvdXJjZVNoYXJlLlRhZ3NF",
            "bnRyeRIMCgRuYW1lGAYgASgJGisKCVRhZ3NFbnRyeRILCgNrZXkYASABKAkS",
            "DQoFdmFsdWUYAiABKAk6AjgBIkEKA1JBTRI6Cg5yZXNvdXJjZV9zaGFyZRgB",
            "IAMoCzIiLm9hazkudHl0aG9uLmF3cy5yYW0uUmVzb3VyY2VTaGFyZWIGcHJv",
            "dG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Ram.ResourceShare), global::Oak9.Tython.Aws.Ram.ResourceShare.Parser, new[]{ "ResourceInfo", "Principals", "AllowExternalPrincipals", "ResourceArns", "Tags", "Name" }, null, null, null, new pbr::GeneratedClrTypeInfo[] { null, }),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Ram.RAM), global::Oak9.Tython.Aws.Ram.RAM.Parser, new[]{ "ResourceShare" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class ResourceShare : pb::IMessage<ResourceShare>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ResourceShare> _parser = new pb::MessageParser<ResourceShare>(() => new ResourceShare());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ResourceShare> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Ram.AwsRamReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceShare() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceShare(ResourceShare other) : this() {
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      principals_ = other.principals_.Clone();
      allowExternalPrincipals_ = other.allowExternalPrincipals_;
      resourceArns_ = other.resourceArns_.Clone();
      tags_ = other.tags_.Clone();
      name_ = other.name_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ResourceShare Clone() {
      return new ResourceShare(this);
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 1;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    /// <summary>Field number for the "principals" field.</summary>
    public const int PrincipalsFieldNumber = 2;
    private static readonly pb::FieldCodec<string> _repeated_principals_codec
        = pb::FieldCodec.ForString(18);
    private readonly pbc::RepeatedField<string> principals_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> Principals {
      get { return principals_; }
    }

    /// <summary>Field number for the "allow_external_principals" field.</summary>
    public const int AllowExternalPrincipalsFieldNumber = 3;
    private bool allowExternalPrincipals_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool AllowExternalPrincipals {
      get { return allowExternalPrincipals_; }
      set {
        allowExternalPrincipals_ = value;
      }
    }

    /// <summary>Field number for the "resource_arns" field.</summary>
    public const int ResourceArnsFieldNumber = 4;
    private static readonly pb::FieldCodec<string> _repeated_resourceArns_codec
        = pb::FieldCodec.ForString(34);
    private readonly pbc::RepeatedField<string> resourceArns_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> ResourceArns {
      get { return resourceArns_; }
    }

    /// <summary>Field number for the "tags" field.</summary>
    public const int TagsFieldNumber = 5;
    private static readonly pbc::MapField<string, string>.Codec _map_tags_codec
        = new pbc::MapField<string, string>.Codec(pb::FieldCodec.ForString(10, ""), pb::FieldCodec.ForString(18, ""), 42);
    private readonly pbc::MapField<string, string> tags_ = new pbc::MapField<string, string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::MapField<string, string> Tags {
      get { return tags_; }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 6;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ResourceShare);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ResourceShare other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      if(!principals_.Equals(other.principals_)) return false;
      if (AllowExternalPrincipals != other.AllowExternalPrincipals) return false;
      if(!resourceArns_.Equals(other.resourceArns_)) return false;
      if (!Tags.Equals(other.Tags)) return false;
      if (Name != other.Name) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      hash ^= principals_.GetHashCode();
      if (AllowExternalPrincipals != false) hash ^= AllowExternalPrincipals.GetHashCode();
      hash ^= resourceArns_.GetHashCode();
      hash ^= Tags.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      principals_.WriteTo(output, _repeated_principals_codec);
      if (AllowExternalPrincipals != false) {
        output.WriteRawTag(24);
        output.WriteBool(AllowExternalPrincipals);
      }
      resourceArns_.WriteTo(output, _repeated_resourceArns_codec);
      tags_.WriteTo(output, _map_tags_codec);
      if (Name.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Name);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      principals_.WriteTo(ref output, _repeated_principals_codec);
      if (AllowExternalPrincipals != false) {
        output.WriteRawTag(24);
        output.WriteBool(AllowExternalPrincipals);
      }
      resourceArns_.WriteTo(ref output, _repeated_resourceArns_codec);
      tags_.WriteTo(ref output, _map_tags_codec);
      if (Name.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Name);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      size += principals_.CalculateSize(_repeated_principals_codec);
      if (AllowExternalPrincipals != false) {
        size += 1 + 1;
      }
      size += resourceArns_.CalculateSize(_repeated_resourceArns_codec);
      size += tags_.CalculateSize(_map_tags_codec);
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ResourceShare other) {
      if (other == null) {
        return;
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      principals_.Add(other.principals_);
      if (other.AllowExternalPrincipals != false) {
        AllowExternalPrincipals = other.AllowExternalPrincipals;
      }
      resourceArns_.Add(other.resourceArns_);
      tags_.MergeFrom(other.tags_);
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            principals_.AddEntriesFrom(input, _repeated_principals_codec);
            break;
          }
          case 24: {
            AllowExternalPrincipals = input.ReadBool();
            break;
          }
          case 34: {
            resourceArns_.AddEntriesFrom(input, _repeated_resourceArns_codec);
            break;
          }
          case 42: {
            tags_.AddEntriesFrom(input, _map_tags_codec);
            break;
          }
          case 50: {
            Name = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            principals_.AddEntriesFrom(ref input, _repeated_principals_codec);
            break;
          }
          case 24: {
            AllowExternalPrincipals = input.ReadBool();
            break;
          }
          case 34: {
            resourceArns_.AddEntriesFrom(ref input, _repeated_resourceArns_codec);
            break;
          }
          case 42: {
            tags_.AddEntriesFrom(ref input, _map_tags_codec);
            break;
          }
          case 50: {
            Name = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class RAM : pb::IMessage<RAM>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<RAM> _parser = new pb::MessageParser<RAM>(() => new RAM());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<RAM> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Ram.AwsRamReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public RAM() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public RAM(RAM other) : this() {
      resourceShare_ = other.resourceShare_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public RAM Clone() {
      return new RAM(this);
    }

    /// <summary>Field number for the "resource_share" field.</summary>
    public const int ResourceShareFieldNumber = 1;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Aws.Ram.ResourceShare> _repeated_resourceShare_codec
        = pb::FieldCodec.ForMessage(10, global::Oak9.Tython.Aws.Ram.ResourceShare.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Aws.Ram.ResourceShare> resourceShare_ = new pbc::RepeatedField<global::Oak9.Tython.Aws.Ram.ResourceShare>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Aws.Ram.ResourceShare> ResourceShare {
      get { return resourceShare_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as RAM);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(RAM other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!resourceShare_.Equals(other.resourceShare_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= resourceShare_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      resourceShare_.WriteTo(output, _repeated_resourceShare_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      resourceShare_.WriteTo(ref output, _repeated_resourceShare_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      size += resourceShare_.CalculateSize(_repeated_resourceShare_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(RAM other) {
      if (other == null) {
        return;
      }
      resourceShare_.Add(other.resourceShare_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            resourceShare_.AddEntriesFrom(input, _repeated_resourceShare_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            resourceShare_.AddEntriesFrom(ref input, _repeated_resourceShare_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
